{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKZV8omI9ornhagC0OgY40",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "W5Vw379YNBX_"
      },
      "outputs": [],
      "source": [
        "def get_fixed_price(rate, discounted_price):\n",
        "    return discounted_price / ((100-rate) * 0.01)\n",
        "\n",
        "rate = int(input(\"할인율은? \"))\n",
        "\n",
        "A_discounted_price = int(input(\"A 상품의 할인된 가격은? \"))\n",
        "B_discounted_price = int(input(\"B 상품의 할인된 가격은? \"))\n",
        "\n",
        "print(\"A 상품의 정가는\", get_fixed_price(rate, A_discounted_price), \"원\")\n",
        "print(\"B 상품의 정가는\", get_fixed_price(rate, B_discounted_price), \"원\")"
      ]
    }
  ]
}