# Mobile Shop CRUD Project

A simple Python console-based Mobile Shop Management system.

## Features
1. Add Mobile
2. Display All Mobiles
3. Search Mobile
4. Update Mobile
5. Delete Mobile
6. Exit

## Data Structure
Each mobile is stored as:
`[id, brand, model, price, quantity]`

Example:
`[101, "Samsung", "Galaxy A55", 35000, 5]`

## CRUD Mapping
- Create → `add_mobile()`
- Read → `display_mobiles()`
- Read/Search → `search_mobile()`
- Update → `update_mobile()`
- Delete → `delete_mobile()`

## How to Run
Python 3.10 or newer is recommended because this project uses `match-case`.

```bash
python mobile_shop_crud.py
```

No external libraries are required.
