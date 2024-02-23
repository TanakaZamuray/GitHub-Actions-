import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")


if __name__ == "__main__":
    main()

name: Aprendiendo GitHub Actions
run-name: ¡Estoy aprendiendo GitHub Actions!
on: [push]
jobs:
  hola-mundo:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Definir variable
        run: echo "USERNAME=${{ github.actor }}" >> $GITHUB_ENV
      - name: Correr script
        run: python hola_mundo.py
