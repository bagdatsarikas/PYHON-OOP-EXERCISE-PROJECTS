{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e2d1e3c3",
   "metadata": {},
   "source": [
    "# object oriented programing exercise"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8196d024",
   "metadata": {},
   "source": [
    "Question 1: Phone Book\n",
    "\n",
    "Create a class that stores people’s names and their phone numbers. The phone book starts empty.\n",
    "\n",
    "The class should have the following methods:\n",
    "\n",
    "add: receives a name and a phone number, and saves them. ✅ (you did this)\n",
    "find: receives a name and returns the phone number. If the name is not in the phone book, return “Not found”.\n",
    "delete: receives a name and removes that contact.\n",
    "show: prints every name and phone number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "233368f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class phonebook():\n",
    "\n",
    "    def __init__(self):\n",
    "        self.phonelist = {}\n",
    "        \n",
    "    def add(self, name, number):\n",
    "        self.phonelist[name] = number\n",
    "        \n",
    "    def find(self,name):\n",
    "        if name in self.phonelist:\n",
    "            return self.phonelist[name]\n",
    "        else:\n",
    "            print(\"no name found\")\n",
    "            \n",
    "    def delete(self, name):\n",
    "        if name in self.phonelist:\n",
    "            del self.phonelist[name]\n",
    "        else: \n",
    "            print(\"name not found\")\n",
    "            \n",
    "    def showphonelist(self):\n",
    "        print(self.phonelist)\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3221fd58",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = phonebook()\n",
    "p.add(\"bag\", \"34-676\")\n",
    "p.add(\"sag\", \"44-55\")\n",
    "p.add(\"del\", \"454-55\")\n",
    "p.delete(\"del\")\n",
    "p.showphonelist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b400f8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "a15c4756",
   "metadata": {},
   "source": [
    "Question 2: Bank Account\n",
    "\n",
    "Create a class called BankAccount. When an account is created, it should receive the owner’s name, and the balance should start at 0.\n",
    "\n",
    "The class should have the following methods:\n",
    "\n",
    "deposit: adds money to the balance. If the amount is 0 or less, print “Invalid amount” and do not change the balance.\n",
    "withdraw: takes money from the balance. If the amount is more than the balance, print “Not enough money” and do not change the balance.\n",
    "show: prints the owner’s name and the balance, for example: Ali has 50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9def8ea1",
   "metadata": {},
   "outputs": [],
   "source": [
    "class bankaccount():\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        self.balance = 0\n",
    "        \n",
    "    def deposit(self,money):\n",
    "        self.balance = self.balance + money\n",
    "        \n",
    "    def withdraw(self, money):\n",
    "        if money > self.balance:\n",
    "            print(\"not enough money\")\n",
    "        else : \n",
    "            self.balance = self.balance - money\n",
    "            \n",
    "    def showbalance(self):\n",
    "        print(self.name , \"has\", self.balance)\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20639af4",
   "metadata": {},
   "outputs": [],
   "source": [
    "m = bankaccount(\"ali\")\n",
    "m.deposit(100)\n",
    "m.deposit(50)\n",
    "print(m.balance)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "348b88c4",
   "metadata": {},
   "source": [
    "Question 3: Word Counter\n",
    "\n",
    "Create a class called WordCounter. When it is created, it should receive a sentence.\n",
    "\n",
    "The class should have the following methods:\n",
    "\n",
    "word_count: returns how many words are in the sentence.\n",
    "longest_word: returns the longest word in the sentence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4ea82733",
   "metadata": {},
   "outputs": [],
   "source": [
    "class wordcounter():\n",
    "    \n",
    "    def __init__(self, sentence):\n",
    "        self.sentence = sentence \n",
    "        \n",
    "    def countword(self):\n",
    "        self.wordlist = self.sentence.split()\n",
    "        return len(self.wordlist)\n",
    "        \n",
    "        \n",
    "    def largestword(self):\n",
    "        \n",
    "        self.largest = \"\"\n",
    "        for n in self.wordlist:\n",
    "            if len(n) > len(self.largest):\n",
    "                self.largest = n \n",
    "        return self.largest\n",
    "\n",
    "w = wordcounter(\"you did a good job\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9cfce989",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "w.countword()\n",
    "w.largestword()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f99db3c0",
   "metadata": {},
   "source": [
    "Question 4: Restaurant Menu\n",
    "\n",
    "Create a class called Menu that stores food names and their prices. The menu starts empty.\n",
    "\n",
    "The class should have the following methods:\n",
    "\n",
    "add: receives a food name and its price, and adds it to the menu.\n",
    "total: receives a list of food names (an order) and returns the total price of the order. If a food appears twice in the list, it should be counted twice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "990946b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "class Menu:\n",
    "    def __init__(self):\n",
    "        self.items = {}\n",
    "\n",
    "    def add(self, food, price):\n",
    "        self.items[food] = price\n",
    "\n",
    "    def total(self, order):\n",
    "        total = 0\n",
    "        for food in order:\n",
    "            total = total + self.items[food]\n",
    "        return total\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    m = Menu()\n",
    "    m.add(\"burger\", 10)\n",
    "    m.add(\"fries\", 4)\n",
    "    print(m.total([\"burger\", \"fries\", \"fries\"])) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e82d324",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
