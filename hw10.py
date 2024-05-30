{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMPN6oUywfVEhoArBxA6vPM",
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
        "<a href=\"https://colab.research.google.com/github/Nuroka/python_homework/blob/main/hw10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EIEo_BSmXyEa"
      },
      "outputs": [],
      "source": [
        "import pickle\n",
        "import os\n",
        "\n",
        "def input_scores():\n",
        "    scores = []\n",
        "    cnt = 1\n",
        "    while True:\n",
        "        score = input(f'#{cnt}? ')\n",
        "        if score == '-1':\n",
        "            break\n",
        "        scores.append(int(score))\n",
        "        cnt += 1\n",
        "    return scores\n",
        "\n",
        "def get_average(scores):\n",
        "    sum_ = sum(scores)\n",
        "    average = sum_/len(scores)\n",
        "    return average\n",
        "\n",
        "def show_scores(scores):\n",
        "    print('개인점수: ', end='')\n",
        "    for score in scores:\n",
        "        print(score, end=' ')\n",
        "\n",
        "\n",
        "filepath = 'score.bin'\n",
        "\n",
        "if os.path.exists(filepath):\n",
        "    with open(filepath, 'rb') as file:\n",
        "        print('[파일 읽기]\\n')\n",
        "        print('[점수 출력]')\n",
        "        scores = pickle.load(file)\n",
        "        show_scores(scores)\n",
        "        print(f'평균: {get_average(scores):.1f}')\n",
        "\n",
        "else:\n",
        "    with open(filepath, 'wb') as file:\n",
        "        print('[점수 입력]')\n",
        "        scores = input_scores()\n",
        "        print('[점수 출력]')\n",
        "        show_scores(scores)\n",
        "        print(f'평균: {get_average(scores):.1f}')\n",
        "        pickle.dump(scores, file)"
      ]
    }
  ]
}