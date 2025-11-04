import requests

webhook_url = input("webhook url: ")

def cool(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def embed():
    print("""Basic Text Formatting

    Bold: **text** or __text__
    Italic: *text* or _text_
    Bold & Italic: ***text*** or ___text___
    Strikethrough: ~~text~~
    Underline: __text__ (Often combined with bold, e.g. __**text**__)
    
    Inline code: `code`
    Code block: Use triple backticks (```)
    """)

    titel = input("Choose a title: ")
    if not titel:
        titel = "No title"

    message = cool("Enter your message (hit Enter on an empty line to stop):")
    if not message.strip():
        print("❌ Du kan ikke sende en tom melding.")
        return

    print("Website for hex colours: https://imagecolorpicker.com/")
    colour_input = input("What colour do you want? (Use 0x followed by hex, e.g. 0x3498db. Leave blank for default): ").strip()
    if colour_input:
        try:
            colour = int(colour_input, 16)
            print(f"🎨 Colour set to: #{colour:06X}")
        except ValueError:
            print("❌ Invalid colour. Using default colour.")
            colour = 0x7289DA
    else:
        colour = 0x7289DA

    bilde = input("Do you want an image? (yes/no): ").strip().lower()
    if bilde in ("yes", "y"):
        bilde = input("Link to the image: ").strip()
        if bilde and not bilde.startswith("http"):
            print("⚠️ linkimage isn't valid.")
    else:
        bilde = None

    data = {
        "username": "Webhook Bot",
        "embeds": [
            {
                "title": titel,
                "description": message,
                "color": colour,
                **({"image": {"url": bilde}} if bilde else {})
            }
        ]
    }

    response = requests.post(webhook_url, json=data)
    print("✅ Meldingen ble sendt!" if response.status_code == 204 else f"❌ Feil: {response.status_code}")

def normal():
    message = input("What do you want to send?: ").strip()
    if not message:
        print("❌ Can't send the message.")
        return

    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)
    print("✅ Meldingen ble sendt!" if response.status_code == 204 else f"❌ Feil: {response.status_code}")

while True:
    print()
    print("\n----------------------------------------------------")
    print(" A SIMPLE DISCORD WEBHOOK SENDER made by NOKONIKO")
    print("----------------------------------------------------")
    print("""
    OPTIONS: 1. single message 
             2. with embed
    """)
    ask = input("Do you want to send an embed? (yes/no/exit): ").strip().lower()
    if ask in ("yes", "y"):
        embed()
    elif ask in ("no", "n"):
        normal()
    elif ask in ("exit", "e", "q"):
        print("👋 Closing...")
        break
    else:
        print("❌ Inavlid choice.")

