# Scalizer Stock Analytic Costs Skip MTO

Skip the analytic cost of MTO moves per operation type.

## Features

- New _Skip MTO Moves_ option on the operation types having _Analytic Costs_ checked.
- When checked, the moves supplied on order (MTO) and the purchase receipts feeding them do not create analytic
  entries: their analytic cost comes from the vendor bill.
- The other moves of the operation type keep generating their analytic entries.

## Usage

1. Open an operation type with _Analytic Costs_ checked.
2. Check _Skip MTO Moves_ to leave the analytic cost of MTO moves to the vendor bill.

## Authors

- Scalizer

## Maintainers

This module is maintained by [Scalizer](https://www.scalizer.fr).

![Scalizer](./static/description/logo.png)
