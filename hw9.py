{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5BiSmeRcftC0c2ITFAm8K",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "M2m4-BsyAD7C"
      },
      "outputs": [],
      "source": [
        "class Point:\n",
        "\n",
        "    def __init__(self, x = 0 , y = 0):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "\n",
        "    def show(self):\n",
        "        print(f\"({self.x}, {self.y})\")\n",
        "\n",
        "    def set(self, x, y):\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "        return True\n",
        "\n",
        "    def get(self):\n",
        "        return (self.x, self.y)\n",
        "\n",
        "\n",
        "class Rectangle:\n",
        "\n",
        "    def __init__(self, x1, y1, x2, y2):\n",
        "        self.lt = Point(x1, y1)\n",
        "        self.rb = Point(x2, y2)\n",
        "        # 항상 lt가 rb보다 왼쪽 상단에 있다고 가정\n",
        "        # x1 < x2, y1 < y2\n",
        "\n",
        "    def show(self):\n",
        "        self.lt.show()\n",
        "        self.rb.show()\n",
        "\n",
        "    def getWidth(self):\n",
        "        return self.rb.x - self.lt.x\n",
        "\n",
        "    def getHeight(self):\n",
        "        return self.rb.y - self.lt.y\n",
        "\n",
        "    def getArea(self):\n",
        "        return self.getWidth() * self.getHeight()\n",
        "\n",
        "    def getPerimeter(self):\n",
        "        return (self.getWidth() + self.getHeight()) * 2\n",
        "\n",
        "\n",
        "\n",
        "# 주 프로그램부\n",
        "r1 = Rectangle(5, 5, 20, 10)\n",
        "a = r1.getArea()\n",
        "p = r1.getPerimeter()\n",
        "r1.show()\n",
        "print(f'\\n넓이는 {a}, 둘레는 {p}')"
      ]
    }
  ]
}