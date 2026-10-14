# currency-converter
I built this currency converter as my solution to a travel agent task. The code, test plan and documentation are all here.

## The story behind it

This was one of my first full programs, built in the first term of my T Level
in Digital Software Development 

The brief cast me as a junior developer working for a local travel agent. Staff
needed a quick way to tell a customer exactly what a currency exchange would
cost them: how much foreign money they would get, what fee the agent would
charge, and what the total would be in pounds. The agent only deals in five
currencies, charges a fee that gets smaller as the amount gets bigger, gives
staff 5% off, and will not exchange more than £2,500 in one go.

Testing caught a real bug. I had written the fee bands with `==` instead of
range comparisons, so `GBP == 300` only matched an amount of exactly £300, and
an amount like £500 fell through every band. Testing also showed people typed
"y" and "Y" as well as "yes", so I made the staff question accept all of them.

## What it does

- Takes an amount in GBP, up to £2,500
- Converts it into USD, EUR, BRL, JPY or TRY using rates held in a dictionary
- Charges a transaction fee in bands: 3.5% under £300, falling to 1.5% from
  £2,000
- Takes 5% off the total if the customer is a member of staff
- Prints a transaction summary
- Asks again if the amount or currency is not valid, instead of crashing

## Running it

```bash
python3 scripts/currency_converter.py
```

It only uses the Python standard library, so there is nothing to install.


## What the documents found

**Business context.** A program does this job better than a calculator and a
rate table: it is faster, it does not make arithmetic mistakes, and every
customer gets the same fees and discounts. The costs are the time to build and
test it, depending on the computer working, and someone having to update the
rates by hand. Whether to keep it on one machine or put it online comes down to
security, internet access and whether the agent needs live rates.

**Flowchart.** I planned the order before writing any code: take the amount
and check it is between £0 and £2,500, show the currencies and check the
choice, convert, add the fee, ask if the customer is staff, then print the
summary. If either check fails, the user tries again. The program follows the
same steps.

**Test plan.** All ten cases passed. They cover normal conversions, the fee at
the £300 and £750 boundaries, the staff discount, amounts over the limit,
negative amounts, a currency code that does not exist, and "Y" typed in
capitals.

**Evaluation.** The program meets everything the brief asked for. Splitting it
into functions means the rates or fee bands can be changed without touching the
rest. The evaluation also records what changed during development: the fee band
fix, loops that ask again after a bad input, and the staff question accepting
"y" as well as "yes".

## What I would do differently

- The fee bands stop at £299.99 and start again at £300, so an amount in
  between, like £299.995, matches no band and crashes the program. The bands
  should run straight into each other.
- The exchange rates are typed into the code. A real version would fetch
  today's rates.
- The test plan is run by hand. Next I want to turn those ten cases into
  automated tests with pytest.

Thanks for stopping by. Bye for now.