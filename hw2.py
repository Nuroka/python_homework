{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOvnOE1IKZNYrkg9JZqCeH9"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1mTyxJxTE6uh"
      },
      "outputs": [],
      "source": [
        "def exchange(money):\n",
        "    n500 = money // 500\n",
        "    money %= 500\n",
        "\n",
        "    n100 = money // 100\n",
        "    money %= 100\n",
        "\n",
        "    n50 = money // 50\n",
        "    money %= 50\n",
        "\n",
        "    n10 = money // 10\n",
        "\n",
        "    print(f\"500원 동전의 개수: {n500}\\n100원 동전의 개수: {n100}\\n50원 동전의 개수: {n50}\\n10원 동전의 개수: {n10}\")\n",
        "\n",
        "def get_integer(prompt):\n",
        "    money = int(input(prompt))\n",
        "    return money\n",
        "\n",
        "money = get_integer(\"동전으로 교환하고자 하는 금액은? \")\n",
        "exchange(money)"
      ]
    }
  ]
}