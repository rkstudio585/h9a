from rich.console import Console
from rich.text import Text
import pyfiglet

def create_banner():
    # Step 1: Create the main banner
    banner = pyfiglet.figlet_format("H9A")
    sub_name = "How Many 9 In 1 to 100"
    console.print(Text(banner, style="bold magenta"))
    console.print(Text(sub_name, style="bold cyan"))

def calculate_nines():
    # Step 2: Calculate occurrences of 9 in the ones place
    ones_place = 10  # 9 appears in the ones place: 9, 19, 29, ..., 99
    console.print(f"[bold blue]Step 2: 9 appears {ones_place} times in the ones place.[/bold blue]")

    # Step 3: Calculate occurrences of 9 in the tens place
    tens_place = 9   # 9 appears in the tens place: 90, 91, 92, ..., 99
    console.print(f"[bold blue]Step 3: 9 appears {tens_place} times in the tens place.[/bold blue]")

    # Step 4: Calculate total occurrences of 9
    total_nines = ones_place + tens_place
    console.print(f"[bold blue]Step 4: Total occurrences of 9 = {total_nines}.[/bold blue]")

    return total_nines

def detailed_explanation():
    # Step 5: Provide a detailed explanation of the calculation
    explanation = (
        "\n[bold cyan]Explanation:[/bold cyan]\n"
        "1. In the ones place: The digit 9 appears in numbers like 9, 19, 29, ..., 99.\n"
        "2. In the tens place: The digit 9 appears in numbers like 90, 91, 92, ..., 99.\n"
        "3. Total occurrences are calculated by adding these together."
    )
    console.print(explanation)

if __name__ == "__main__":
    console = Console()

    # Display banner
    create_banner()

    # Perform calculation with detailed steps
    console.print("\n[bold green]Calculating step by step...[/bold green]", style="bold yellow")
    total_nines = calculate_nines()

    # Display detailed explanation
    detailed_explanation()

    # Display final result
    console.print(
        f"\n[bold white]Final Result: In the range 1 to 100, the digit '9' appears [bold red]{total_nines}[/bold red] times![/bold white]",
        style="bold green",
    )
  
