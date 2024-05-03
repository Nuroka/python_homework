{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN0o/9Suj6225Yid1Q3R7s+",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UqLCY31V6K7G",
        "outputId": "2ea2254c-ea14-4529-8637-391ccb4f8b4c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[구입]\n"
          ]
        }
      ],
      "source": [
        "shopping_bag = {}\n",
        "\n",
        "print(\"[구입]\")\n",
        "while True:\n",
        "    item = input(\"상품명? \")\n",
        "\n",
        "    if item == '':\n",
        "        break\n",
        "    else:\n",
        "        quantity = int(input(\"수량은? \"))\n",
        "\n",
        "        shopping_bag[item] = quantity\n",
        "        print(f'장바구니에 {item} {quantity}개가 담겼습니다.')\n",
        "\n",
        "print(f\">>> 장바구니 보기: {shopping_bag}\")\n",
        "\n",
        "print(\"[검색]\")\n",
        "item = input(\"장바구니에서 확인하고자 하는 상품은? \")\n",
        "if item in shopping_bag:\n",
        "    print(f\"{item}은(는) {shopping_bag[item]}개 담겨 있습니다.\")\n",
        "else:\n",
        "    print(f\"{item}은(는) 장바구니에 없습니다.\")"
      ]
    }
  ]
}