# Scalizer Project MRP Stock Account

Analytic costs on the component pickings of manufacturing orders.

## Features

- The component picking of a multi-step manufacturing order (e.g. _Pick Components_) gets the project of the
  manufacturing order, so that its moves generate analytic entries when _Analytic Costs_ is checked on its operation
  type.
- The analytic entries of these internal moves are booked as a cost (negative amount), like the outgoing moves.

## Usage

1. Set the warehouse manufacturing in 2 or 3 steps.
2. Check _Analytic Costs_ on the component picking operation type.
3. Confirm a manufacturing order with a project: validating its component picking generates the analytic costs on the
   project.

## Authors

- Scalizer

## Maintainers

This module is maintained by [Scalizer](https://www.scalizer.fr).

![Scalizer](./static/description/logo.png)
