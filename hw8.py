{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN47CO8YhLLxH+YrRYfXfHr",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "AHxpbTg6oCzT"
      },
      "outputs": [],
      "source": [
        "def buy(dict):\n",
        "    print(\"[구입]\")\n",
        "    item = input(\"상품명? \")\n",
        "\n",
        "    if item:\n",
        "        quantity = int(input(\"수량은? \"))\n",
        "        dict[item] = quantity\n",
        "        print(f'장바구니에 {item} {quantity}개가 담겼습니다.\\n')\n",
        "        return True\n",
        "    else:\n",
        "        print()\n",
        "        return False\n",
        "\n",
        "def show(dict):\n",
        "    print(f\">>> 장바구니 보기: {dict}\\n\")\n",
        "\n",
        "def find(dict):\n",
        "    print(\"[검색]\")\n",
        "    item = input(\"장바구니에서 확인하고자 하는 상품은? \")\n",
        "\n",
        "    if item in dict:\n",
        "        print(f\"{item}은(는) {dict[item]}개 담겨 있습니다.\")\n",
        "    else:\n",
        "        print(f\"장바구니에 {item}은(는) 없습니다.\")\n",
        "\n",
        "\n",
        "shopping_bag = {}\n",
        "\n",
        "while True:\n",
        "    if buy(shopping_bag) == False:\n",
        "        break\n",
        "\n",
        "show(shopping_bag)\n",
        "find(shopping_bag)"
      ]
    }
  ]
}