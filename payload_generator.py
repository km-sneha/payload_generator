import base64
import urllib.parse
import hashlib
from colorama import Fore, Style
import pyfiglet
from rich.console import Console
from rich.progress import track
import time

# Console for colorful output
console = Console()

def welcome_screen():
    banner = pyfiglet.figlet_format("Payload Generator")
    console.print(f"[bold magenta]{banner}[/bold magenta]")
    console.print("[bold cyan]Developed by: Sneha KM[/bold cyan]")
    console.print("[bold cyan]GitHub: https://github.com/km-sneha[/bold cyan]\n")
    console.print("[bold green]Welcome to the Custom Payload Generator![/bold green] 🚀\n")

# Encoding functions
def encode_base64(payload):
    return base64.b64encode(payload.encode()).decode()

def encode_url(payload):
    return urllib.parse.quote(payload)

def encode_hex(payload):
    return payload.encode().hex()

def encode_base32(payload):
    return base64.b32encode(payload.encode()).decode()

def encode_md5(payload):
    return hashlib.md5(payload.encode()).hexdigest()

def encode_sha256(payload):
    return hashlib.sha256(payload.encode()).hexdigest()

# Decoding functions
def decode_base64(payload):
    return base64.b64decode(payload).decode()

def decode_url(payload):
    return urllib.parse.unquote(payload)

def decode_hex(payload):
    bytes_object = bytes.fromhex(payload)
    return bytes_object.decode()

def decode_base32(payload):
    return base64.b32decode(payload).decode()

def decode_md5(payload):
    console.print("[bold red]MD5 is a one-way hash and cannot be decoded.[/bold red]")
    return None

def decode_sha256(payload):
    console.print("[bold red]SHA256 is a one-way hash and cannot be decoded.[/bold red]")
    return None

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
    console.print(f"[bold green]Payload saved to {filename}![/bold green]")

def animated_progress(task_name, duration=3):
    for _ in track(range(duration), description=f"[bold yellow]{task_name}[/bold yellow]"):
        time.sleep(1)

def main():
    welcome_screen()
    while True:
        console.print("\n[bold magenta]Choose an option:[/bold magenta]")
        console.print("[1] Encode Payload")
        console.print("[2] Decode Payload")
        console.print("[3] Exit\n")

        choice = input(Fore.CYAN + "Enter your choice (1-3): " + Style.RESET_ALL)
        if choice not in {'1', '2', '3'}:
            console.print("[bold red]Invalid choice! Please select a valid option.[/bold red]")
            continue

        if choice == '3':
            console.print("[bold cyan]Thank you for using the Custom Payload Generator![/bold cyan] 🎉")
            break

        console.print("\n[bold magenta]Choose an encoding method:[/bold magenta]")
        console.print("[1] Base64 Encoding/Decoding")
        console.print("[2] URL Encoding/Decoding")
        console.print("[3] Hex Encoding/Decoding")
        console.print("[4] Base32 Encoding/Decoding")
        console.print("[5] MD5 Encoding (Hashing, no decoding)")
        console.print("[6] SHA256 Encoding (Hashing, no decoding)\n")

        encoding_choice = input(Fore.CYAN + "Enter your choice (1-6): " + Style.RESET_ALL)
        if encoding_choice not in {'1', '2', '3', '4', '5', '6'}:
            console.print("[bold red]Invalid encoding choice! Please select a valid option.[/bold red]")
            continue

        if encoding_choice == '5' or encoding_choice == '6':
            payload = input(Fore.GREEN + "Enter the payload to encode: " + Style.RESET_ALL)
            console.print("\n[bold yellow]Encoding in progress...[/bold yellow]")
            animated_progress("Encoding", 3)

            if encoding_choice == '5':
                encoded_payload = encode_md5(payload)
                console.print(f"\n[bold green]MD5 Encoded Payload:[/bold green] {encoded_payload}")
            elif encoding_choice == '6':
                encoded_payload = encode_sha256(payload)
                console.print(f"\n[bold green]SHA256 Encoded Payload:[/bold green] {encoded_payload}")

        else:
            operation = input(Fore.YELLOW + "Do you want to Encode or Decode? (e/d): " + Style.RESET_ALL).lower()
            if operation not in {'e', 'd'}:
                console.print("[bold red]Invalid operation! Please select 'e' for encode or 'd' for decode.[/bold red]")
                continue

            payload = input(Fore.GREEN + "Enter the payload: " + Style.RESET_ALL)
            if not payload.strip():
                console.print("[bold red]Payload cannot be empty![/bold red]")
                continue

            console.print("\n[bold yellow]Processing...[/bold yellow]")
            animated_progress("Processing", 3)

            if encoding_choice == '1':  # Base64
                if operation == 'e':
                    encoded_payload = encode_base64(payload)
                    console.print(f"\n[bold green]Base64 Encoded Payload:[/bold green] {encoded_payload}")
                else:
                    decoded_payload = decode_base64(payload)
                    if decoded_payload:
                        console.print(f"\n[bold green]Decoded Base64 Payload:[/bold green] {decoded_payload}")
            elif encoding_choice == '2':  # URL
                if operation == 'e':
                    encoded_payload = encode_url(payload)
                    console.print(f"\n[bold green]URL Encoded Payload:[/bold green] {encoded_payload}")
                else:
                    decoded_payload = decode_url(payload)
                    console.print(f"\n[bold green]Decoded URL Payload:[/bold green] {decoded_payload}")
            elif encoding_choice == '3':  # Hex
                if operation == 'e':
                    encoded_payload = encode_hex(payload)
                    console.print(f"\n[bold green]Hex Encoded Payload:[/bold green] {encoded_payload}")
                else:
                    decoded_payload = decode_hex(payload)
                    console.print(f"\n[bold green]Decoded Hex Payload:[/bold green] {decoded_payload}")
            elif encoding_choice == '4':  # Base32
                if operation == 'e':
                    encoded_payload = encode_base32(payload)
                    console.print(f"\n[bold green]Base32 Encoded Payload:[/bold green] {encoded_payload}")
                else:
                    decoded_payload = decode_base32(payload)
                    console.print(f"\n[bold green]Decoded Base32 Payload:[/bold green] {decoded_payload}")

        save_option = input(Fore.YELLOW + "\nDo you want to save this payload to a file? (y/n): " + Style.RESET_ALL)
        if save_option.lower() == 'y':
            filename = input(Fore.CYAN + "Enter the filename (e.g., payload.txt): " + Style.RESET_ALL)
            save_to_file(encoded_payload if operation == 'e' else decoded_payload, filename)

        continue_option = input(Fore.YELLOW + "\nDo you want to encode/decode another payload? (y/n): " + Style.RESET_ALL)
        if continue_option.lower() != 'y':
            console.print("[bold cyan]Goodbye! See you next time![/bold cyan] 👋")
            break

if __name__ == "__main__":
    main()
