import sys
from typing import List, Optional, Dict
import math
from colorama import Fore, Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from user_scanner.core.result import Result, Status
from user_scanner.core.helpers import ScanConfig

if sys.platform == "win32":
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

console = Console(legacy_windows=False)


def display_scan_results(
    results: List[Result],
    configs: Optional[ScanConfig] = None,
    target: str = "",
    is_email: bool = False,
):
    """
    Renders scan results cleanly side-by-side:
    - Left side: Found / Registered results with metadata tree
    - Right side: Skipped (loud) modules
    Not like a table: uses clean rounded panels.
    """
    hits = [r for r in results if r.is_found()]
    skipped = [r for r in results if r.status == Status.SKIPPED]

    # Format Left Side (Found / Registered Results)
    res_lines = []
    if not hits:
        res_lines.append(f"[yellow]No registered accounts found under scanned modules.[/yellow]")
        p_res = Panel(
            "\n".join(res_lines).rstrip(),
            title=f"[bold yellow]RESULTS / REGISTERED (0)[/bold yellow]",
            subtitle=f"[dim]Target: {target}[/dim]" if target else None,
            border_style="yellow",
            box=box.ROUNDED,
        )
    else:
        from collections import defaultdict
        grouped = defaultdict(list)
        for r in hits:
            cat = (r.category or "Other").capitalize()
            grouped[cat].append(r)

        for cat, items in sorted(grouped.items()):
            res_lines.append(f"[bold magenta]== {cat.upper()} ==[/bold magenta]")
            for r in items:
                site_name = r.site_name
                status_label = r.status.to_label(r.is_email)
                url_str = f" [dim][{r.url}][/dim]" if (configs and configs.verbose and r.url) else ""
                res_lines.append(
                    f"  [bold green]✔[/bold green] [bold white]{site_name}[/bold white]{url_str}: [green]{status_label}[/green]"
                )

                # Extra metadata and tree branches
                display_items = list((r.extra or {}).items()) + list((r.media or {}).items())
                for i, (k, v) in enumerate(display_items):
                    conn = "└──" if i == len(display_items) - 1 else "├──"
                    res_lines.append(f"      [cyan]{conn}[/cyan] [white]{k}[/white]: [cyan]{v}[/cyan]")
            res_lines.append("")

        p_res = Panel(
            "\n".join(res_lines).rstrip(),
            title=f"[bold green]RESULTS / REGISTERED ({len(hits)})[/bold green]",
            subtitle=f"[dim]Target: {target}[/dim]" if target else None,
            border_style="green",
            box=box.ROUNDED,
        )

    # Format Right Side (Skipped Modules)
    if skipped:
        inner_skip = Table.grid(expand=True, padding=(0, 1))
        num_skip_cols = 2 if len(skipped) > 8 else 1
        for _ in range(num_skip_cols):
            inner_skip.add_column(ratio=1)

        rows = math.ceil(len(skipped) / num_skip_cols)
        for r in range(rows):
            row_cells = []
            for c in range(num_skip_cols):
                idx = r + c * rows
                if idx < len(skipped):
                    item = skipped[idx]
                    cat_name = (item.category or "").capitalize()
                    cat_badge = f" [dim]({cat_name})[/dim]" if cat_name else ""
                    row_cells.append(f"[yellow]~[/yellow] [white]{item.site_name}[/white]{cat_badge}")
                else:
                    row_cells.append("")
            inner_skip.add_row(*row_cells)

        p_skip = Panel(
            inner_skip,
            title=f"[bold yellow]SKIPPED ({len(skipped)}) - LOUD MODULES[/bold yellow]",
            subtitle="[dim]Type 'loud' to scan[/dim]",
            border_style="yellow",
            box=box.ROUNDED,
        )
    else:
        p_skip = None

    width = console.width or 100
    if p_skip and width >= 80:
        grid = Table.grid(expand=True, padding=(0, 1))
        grid.add_column(ratio=6)
        grid.add_column(ratio=5)
        grid.add_row(p_res, p_skip)
        console.print()
        console.print(grid)
    else:
        console.print()
        console.print(p_res)
        if p_skip:
            console.print()
            console.print(p_skip)

    console.print(
        f"\n[bold cyan][i] Scan complete:[/bold cyan] [green]{len(hits)} hits[/green]"
        + (f", [yellow]{len(skipped)} loud modules skipped[/yellow]" if skipped else "")
    )
    if skipped:
        console.print(f"  [dim]Tip: Type '[bold yellow]loud[/bold yellow]' or run with [bold green]--allow-loud[/bold green] to scan skipped modules.[/dim]")


def display_final_merged_results(
    target_to_results: Dict[str, List[Result]],
):
    """
    Renders the consolidated final results merging all scanned targets and found accounts
    in a single unified master dashboard.
    """
    from collections import defaultdict

    if not target_to_results:
        return

    content_grid = Table.grid(expand=True, padding=(0, 0))
    content_grid.add_column()

    total_all_hits = 0
    num_targets = len(target_to_results)

    for target_idx, (t_name, t_results) in enumerate(target_to_results.items()):
        hits = [r for r in t_results if r.is_found()]
        total_all_hits += len(hits)

        # Target Header
        t_label = "Email" if ("@" in t_name) else "Username"
        hit_str = f"[bold green]{len(hits)} registered accounts found[/bold green]" if hits else "[yellow]0 accounts found[/yellow]"
        content_grid.add_row(f"[bold cyan]Target ({t_label}):[/bold cyan] [bold white]{t_name}[/bold white]  [dim]•[/dim]  {hit_str}\n")

        if not hits:
            content_grid.add_row("  [dim yellow]No accounts found on checked platforms.[/dim yellow]\n")
            continue

        # Group by Category breakdown
        cat_map = defaultdict(list)
        for r in hits:
            cat = (r.category or "Other").capitalize()
            cat_map[cat].append(r)

        cat_summary_parts = []
        for cat, items in sorted(cat_map.items()):
            site_names = ", ".join(sorted([f"[white]{r.site_name}[/white]" for r in items]))
            cat_summary_parts.append(f"  [bold magenta]• {cat.upper()} ({len(items)}):[/bold magenta] {site_names}")

        content_grid.add_row("\n".join(cat_summary_parts) + "\n")

        # Alphabetical 2-column or 3-column checklist
        sorted_hits = sorted(hits, key=lambda r: r.site_name.lower())
        col_count = 3 if (console.width and console.width >= 110) else 2
        plat_grid = Table.grid(expand=True, padding=(0, 2))
        for _ in range(col_count):
            plat_grid.add_column(ratio=1)

        rows = math.ceil(len(sorted_hits) / col_count)
        for r in range(rows):
            row_cells = []
            for c in range(col_count):
                idx = r + c * rows
                if idx < len(sorted_hits):
                    item = sorted_hits[idx]
                    row_cells.append(f"[bold green]✔[/bold green] [bold white]{item.site_name}[/bold white]")
                else:
                    row_cells.append("")
            plat_grid.add_row(*row_cells)

        content_grid.add_row(plat_grid)
        if target_idx < num_targets - 1:
            content_grid.add_row("\n[dim]────────────────────────────────────────────────────────────────────────[/dim]\n")

    # Overall session footer if multiple targets
    if num_targets > 1:
        content_grid.add_row(
            f"\n[bold cyan]Session Total:[/bold cyan] [bold white]{num_targets} targets scanned[/bold white]  [dim]•[/dim]  [bold green]{total_all_hits} total registered accounts discovered[/bold green]"
        )

    panel = Panel(
        content_grid,
        title="[bold green]SHADOWSEEK - CONSOLIDATED FINAL RESULTS[/bold green]",
        subtitle="[dim]Developed by govind[/dim]",
        border_style="green",
        box=box.ROUNDED,
        padding=(1, 2),
    )
    console.print()
    console.print(panel)


def print_interactive_menu():
    """Prints the interactive help and options menu."""
    menu_text = """[bold cyan]Interactive Console Commands:[/bold cyan]
  [white]• Enter any username or email[/white]     Scan target across all platforms
  [white]• [bold cyan]new[/bold cyan] or [bold cyan]1[/bold cyan][/white]                          Scan another user / enter new target
  [white]• [bold magenta]back[/bold magenta] or [bold magenta]b[/bold magenta][/white]                        Go back / reset active target context
  [white]• [bold blue]users[/bold blue] or [bold blue]6[/bold blue][/white]                        List scanned users & switch context
  [white]• [bold yellow]loud[/bold yellow] or [bold yellow]2[/bold yellow][/white]                         Scan skipped loud modules for current target
  [white]• [bold green]export <pdf|json|csv>[/bold green] or [bold green]3[/bold green][/white]    Export scan results to file
  [white]• [bold cyan]summary[/bold cyan] or [bold cyan]5[/bold cyan][/white]                      Display merged final results for all targets
  [white]• [bold cyan]cats[/bold cyan] or [bold cyan]4[/bold cyan][/white]                         List all available categories & modules
  [white]• [bold cyan]clear[/bold cyan][/white]                           Clear the console screen
  [white]• [bold red]exit[/bold red] or [bold red]0[/bold red][/white]                           Quit Shadowseek"""
    p = Panel(menu_text, title="[bold cyan]Shadowseek - Developed by govind[/bold cyan]", border_style="cyan", box=box.ROUNDED)
    console.print(p)
