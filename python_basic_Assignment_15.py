{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4e7ba749",
   "metadata": {},
   "source": [
    "# Assignment 15 Solutions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02fbc443",
   "metadata": {},
   "source": [
    "1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "efd7a821",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3600\n"
     ]
    }
   ],
   "source": [
    "print(60*60)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "278d56de",
   "metadata": {},
   "source": [
    "2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5da4af44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3600\n"
     ]
    }
   ],
   "source": [
    "seconds_per_hour = 60*60\n",
    "print(seconds_per_hour)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86b0ddaa",
   "metadata": {},
   "source": [
    "3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4e65f8a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86400\n"
     ]
    }
   ],
   "source": [
    "minutes_per_hour = 60\n",
    "print(seconds_per_hour*24)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ad021d2",
   "metadata": {},
   "source": [
    "4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f5159b2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86400\n"
     ]
    }
   ],
   "source": [
    "seconds_per_day = 24*60*60\n",
    "print(seconds_per_day)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f164dcf2",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
