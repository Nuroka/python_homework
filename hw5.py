{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPfvTTpaVeT2RE/8+dx4W9n",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8-ZSMsINyDl_"
      },
      "outputs": [],
      "source": [
        "def read_single_digit(integer):\n",
        "    if integer == 0:\n",
        "        return '영'\n",
        "    elif integer == 1:\n",
        "        return '일'\n",
        "    elif integer == 2:\n",
        "        return '이'\n",
        "    elif integer == 3:\n",
        "        return '삼'\n",
        "    elif integer == 4:\n",
        "        return '사'\n",
        "    elif integer == 5:\n",
        "        return '오'\n",
        "    elif integer == 6:\n",
        "        return '육'\n",
        "    elif integer == 7:\n",
        "        return '칠'\n",
        "    elif integer == 8:\n",
        "        return '팔'\n",
        "    elif integer == 9:\n",
        "        return '구'\n",
        "\n",
        "def read_number(num):\n",
        "    num = str(num)\n",
        "\n",
        "    result = ''\n",
        "\n",
        "    result += f\"{read_single_digit(int(num[0]))} \"\n",
        "\n",
        "    if len(num) == 2:\n",
        "        result += f\"{read_single_digit(int(num[1]))}\"\n",
        "\n",
        "    elif len(num) == 3:\n",
        "        result += f\"{read_single_digit(int(num[1]))} \"\n",
        "        result += f\"{read_single_digit(int(num[2]))}\"\n",
        "\n",
        "    return result\n",
        "\n",
        "number = int(input('세 자리 정수 입력: '))\n",
        "result = read_number(number)\n",
        "print(result)"
      ]
    }
  ]
}