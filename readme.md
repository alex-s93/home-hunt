# Home Hunt API

This project is an API for apartments reservation. It allows users to manage apartments (with addresses), make reservations, and leave reviews.

## Features

- **Apartments and Addresses:**
  - Landlords can create and update apartments and their addresses.
  - All users can view apartments.

- **Search and Filtering:**
  - Users can enter keywords to search in apartment titles and descriptions.
  - Filtering by parameters:
    - **Price:** Users can specify a minimum and maximum price.
    - **Location:** Users can specify a city or region in Germany.
    - **Number of rooms:** Users can specify a range for the number of rooms.
    - **Type of housing:** Users can choose the type of housing (apartment, house, studio, etc.).
  - Sorting results:
    - **By price:** Ability to sort by ascending or descending price.
    - **By date added:** Ability to sort by newest or oldest listings.

- **Reservations:**
  - Renters can create and update reservations.
  - Landlords can approve reservations through a dedicated endpoint.
  - Renters can cancel reservations through a dedicated endpoint, but not later than 5 days before the start date.

- **Reviews:**
  - Renters can leave reviews.
  - All users can view reviews.

## Endpoints

### Addresses
- `GET /addresses/` - View existing addresses (Landlords only)
- `POST /addresses/` - Create a new address (Landlords only)
- `GET /addresses/:id/` - Retrieve an address (Landlords only)
- `PUT /addresses/:id/` - Update an address (Landlords only)
- `DELETE /addresses/:id/` - Delete an address (Landlords only)

### Apartments
- `GET /apartments/` - View all apartments
- `POST /apartments/` - Create a new apartment (Landlords only)
- `GET /apartments/:id/` - Retrieve an apartment
- `PUT /apartments/:id/` - Update an apartment (Landlords only)
- `DELETE /apartments/:id/` - Delete an apartment (Landlords only)

### Reservations
- `GET /reservations/` - View all reservations (Renters can view only own reservations, Landlords can view reservations for apartments they own.)
- `POST /reservations/` - Create a new reservation (Renters only)
- `GET /reservations/:id/` - Retrieve a reservation (Renters can view only own reservation, Landlords can view reservation for apartment they own.)
- `PUT /reservations/:id/` - Update a reservation (Renters only)
- `DELETE /reservations/:id/` - Delete a reservation (Renters only)
- `PUT /reservations/:id/approve/` - Approve a reservation (Landlords only)
- `PUT /reservations/:id/cancel/` - Cancel a reservation (Renters only, must be more than 5 days before the start date)

### Reviews
- `GET /reviews/` - View all reviews
- `POST /reviews/` - Create a new review (Renters only)
- `GET /reviews/:id/` - Retrieve a review
- `PUT /reviews/:id/` - Update a review (Renters only)
- `DELETE /reviews/:id/` - Delete a review (Renters only)


## Permissions

- **Landlords:**
  - Can create and update apartments and addresses.
  - Can approve reservations through a dedicated endpoint.

- **Renters:**
  - Can create and update reservations.
  - Can cancel reservations through a dedicated endpoint, but not later than 5 days before the start date.
  - Can leave reviews.

- **All Users:**
  - Can view all apartments and reviews.

## Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:alex-s93/home-hunt.git
    ```
2. Navigate to the project directory:
    ```sh
    cd HomeHunt
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```
5. Run the development server:
    ```sh
    python manage.py runserver
    ```   