{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP46WWw6KlGddR+3JQ1IKR6",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u7ZL4DxKdqUE",
        "outputId": "552c0890-7a8f-4414-ebc5-2a9fe675b901"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input his/her name: jessica sadfkls sdakflsdaj\n",
            "---------------------------------\n",
            "Hello jessica sadfkls sdakflsdaj,\n",
            "Welcome to Seoul.\n",
            "---------------------------------\n"
          ]
        }
      ],
      "source": [
        "def rep_char(c, n):\n",
        "    print(c * n)\n",
        "\n",
        "def draw_line_string(string):\n",
        "    msg1 = f\"Hello {string},\"\n",
        "    msg2 = \"Welcome to Seoul.\"\n",
        "\n",
        "    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)\n",
        "\n",
        "    rep_char('-', nstr)\n",
        "    print(msg1)\n",
        "    print(msg2)\n",
        "    rep_char('-', nstr)\n",
        "\n",
        "name = input(\"Input his/her name: \")\n",
        "\n",
        "draw_line_string(name)"
      ]
    }
  ]
}