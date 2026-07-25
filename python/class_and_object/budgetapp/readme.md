# Budget App

A command-line budget tracking system in Python. It tracks deposits, withdrawals, and transfers across multiple spending categories, and generates an ASCII bar chart showing the percentage of total spending contributed by each category.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Class Design: `Category`](#class-design-category)
- [Function Design: `create_spend_chart`](#function-design-create_spend_chart)
- [Usage Example](#usage-example)
- [Spend Chart Example](#spend-chart-example)
- [Design Notes](#design-notes)
- [Known Limitations](#known-limitations)
- [Running Tests](#running-tests)
- [Project Origin](#project-origin)
- [License](#license)

## Overview

The app models a personal budget as a set of independent `Category` objects (e.g. Food, Clothing, Auto). Each category maintains its own transaction ledger. Money can be deposited, withdrawn, or transferred between categories, and a standalone function renders a text-based bar chart comparing spending across all categories.

No external dependencies — pure Python 3 standard library.

## Project Structure

```
.
└── main.py   # Category class + create_spend_chart function
```

This is a single-file project by design (matches the lab's scope). If you export the accompanying test suite from the original lab environment, add it alongside as `test_module.py`.

## Features

- Deposit and withdraw funds per category, with optional transaction descriptions
- Transfer funds directly between two categories (auto-generates linked ledger entries on both sides)
- Balance and available-funds checks before any withdrawal or transfer is allowed
- Formatted ledger printout for any category (fixed-width columns, right-aligned amounts)
- ASCII bar chart comparing percentage-of-spend across up to four categories

## Class Design: `Category`

| Method | Signature | Behavior |
|---|---|---|
| `__init__` | `(self, name)` | Sets `self.name`, initializes `self.ledger = []` |
| `deposit` | `(self, amount, description="")` | Appends `{"amount": amount, "description": description}` to the ledger |
| `withdraw` | `(self, amount, description="")` | Appends a **negative** amount if funds are sufficient; returns `True`/`False` |
| `get_balance` | `(self)` | Returns `sum()` of all ledger amounts |
| `transfer` | `(self, amount, other_category)` | Withdraws from self as `"Transfer to {other}"`, deposits into target as `"Transfer from {self}"`; returns `True`/`False` |
| `check_funds` | `(self, amount)` | Returns `False` if `amount > balance`, else `True`. Used internally by both `withdraw` and `transfer` — single source of truth for the funds check |
| `__str__` | `(self)` | Renders the formatted ledger (see below) |

Ledger entries are plain dicts: `{"amount": float, "description": str}`.

### Printed format

- **Title line:** category name centered in a 30-character line of `*`
- **Ledger lines:** description left-aligned to 23 characters (longer strings are truncated), amount right-aligned to 7 characters with 2 decimal places
- **Total line:** `Total: {balance:.2f}`

## Function Design: `create_spend_chart`

Standalone function (not a method) — `create_spend_chart(categories: list[Category]) -> str`. Tested with up to four categories.

Steps:
1. Sum only **withdrawals** (negative ledger amounts) per category — deposits are excluded from the percentage calculation entirely
2. Convert each category's spend to a percentage of total spend across all categories, then **round down to the nearest 10**
3. Draw the y-axis from 100 to 0 in steps of 10, placing an `o` in each row where that category's percentage meets or exceeds the row value
4. Draw a horizontal line two characters past the last bar
5. Write each category name vertically underneath its bar

## Usage Example

```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
```

Output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## Spend Chart Example

```python
print(create_spend_chart([food, clothing, auto]))
```

Output:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Design Notes

The chart's spacing is the trickiest part of the spec — it's easy to get each section individually right and still have the whole thing misaligned. A few non-obvious decisions worth documenting:

- **Bar rows** (`f"{i:>3}| "` then `"o  "` / `"   "` per category) give each category a fixed 3-character column, so bars stay aligned regardless of how many categories are passed in.
- **Horizontal line** uses a 4-space left prefix (`"    "`) to match the y-axis label width (`" 90|"` = 4 characters), followed by `3 * len(categories) + 1` dashes — the `+1` is what pushes the line two characters past the final bar.
- **Vertical name rows** use a **5-space** left prefix, not 4. The bar column's first `o` sits one character further right than the horizontal line's first dash (because of the leading `| ` on bar rows vs. the bare `-` on the line row), so the name column has to shift by one extra space to land under the bars correctly. Getting this prefix wrong by a single character silently misaligns every name row while leaving every other test passing — worth remembering if this ever needs to be modified.
- Percentages are calculated from **withdrawals only**; if a category has deposits but no withdrawals, it contributes `0%` and draws no bar.

## Known Limitations

- **Amount field width:** the ledger printout formats amounts as `{amount:>7.2f}` — a fixed 7-character field. Amounts of roughly 100,000 or more (or very large negative values) will exceed this width and break column alignment. The spec doesn't define behavior for this case, and the current implementation doesn't guard against it — flagging this now rather than letting it fail silently later.
- **Zero total spend:** if no category has any withdrawals, `total_spent` is `0` and the percentage calculation (`amount / total_spent`) will raise a `ZeroDivisionError`. Not handled.
- **Description truncation** is silent — descriptions longer than 23 characters are cut with no indication in the output that truncation happened.

## Running Tests

This project was built and verified against the automated test suite provided in the original lab environment. If you have `test_module.py` alongside `main.py`:

```bash
python -m unittest test_module -v
```

## Project Origin

This project was built as a lab exercise for the **freeCodeCamp Scientific Computing with Python** certification. The class/function specification, method signatures, and exact output formatting were provided by the assignment — the implementation is original, but the design itself is not.

## License

No license has been chosen yet. If you intend to make this public, consider adding an [MIT License](https://choosealicense.com/licenses/mit/) or similar — that's your call to make, not something to leave undecided by default.
