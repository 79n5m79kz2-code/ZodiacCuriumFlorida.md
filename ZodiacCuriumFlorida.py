{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMDERTIIpGL2VdP7W0eNgFY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/79n5m79kz2-code/ZodiacCuriumFlorida.md/blob/main/ZodiacCuriumFlorida.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vjvsN76F9cuu",
        "outputId": "a12452be-4c7c-4e73-bb8c-6d986471ca2d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== Chinese Zodiac Finder ===\n",
            "Enter your year of birth: 2012\n",
            "\n",
            "Your Chinese Zodiac Sign for the year 2012 is: Dragon (龙 / Lóng)\n"
          ]
        }
      ],
      "source": [
        "# zodiacSectionLN.py\n",
        "# Program to determine Chinese Zodiac Sign based on year of birth\n",
        "# Baseline year: 1900 = Rat\n",
        "\n",
        "def main():\n",
        "    print(\"=== Chinese Zodiac Finder ===\")\n",
        "\n",
        "    # a. Ask the user to enter a year of birth\n",
        "    try:\n",
        "        year = int(input(\"Enter your year of birth: \"))\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter a valid year.\")\n",
        "        return\n",
        "\n",
        "    # b. & c. Validate user input - should not be earlier than 1900\n",
        "    if year < 1900:\n",
        "        print(\"Invalid year. Year must not be earlier than 1900.\")\n",
        "        return # stop/abort the program\n",
        "\n",
        "    # d. Determine Chinese Zodiac Sign\n",
        "    # 1900 = Rat. Zodiac repeats every 12 years\n",
        "    zodiac_list = [\n",
        "        \"Rat (鼠 / Shǔ)\",\n",
        "        \"Ox (牛 / Niú)\",\n",
        "        \"Tiger (虎 / Hǔ)\",\n",
        "        \"Rabbit (兔 / Tù)\",\n",
        "        \"Dragon (龙 / Lóng)\",\n",
        "        \"Snake (蛇 / Shé)\",\n",
        "        \"Horse (马 / Mǎ)\",\n",
        "        \"Goat (羊 / Yáng)\",\n",
        "        \"Monkey (猴 / Hóu)\",\n",
        "        \"Rooster (鸡 / Jī)\",\n",
        "        \"Dog (狗 / Gǒu)\",\n",
        "        \"Pig (猪 / Zhū)\"\n",
        "    ]\n",
        "\n",
        "    index = (year - 1900) % 12\n",
        "    zodiac = zodiac_list[index]\n",
        "\n",
        "    # e. Output\n",
        "    print(f\"\\nYour Chinese Zodiac Sign for the year {year} is: {zodiac}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}