const { Model } = require('objection');
const config = require("./knexfile.js")[process.env.NODE_ENV || "development"];
const knex = require("knex")(config);

Model.knex(knex);

// The examples aim to be as simple as possible. Remember to add .catch() to handle errors in a real application.

// Example 1: Work with a single entity
const Customer = require("./models/Customer.js");

Customer.query().max("customerNumber").first().then((max) => {
    const highestCustomerNumber = max['max(`customerNumber`)'];

    const customerToCreate = {
        customerNumber: highestCustomerNumber + 1,
        customerName: "John", 
        contactFirstName: "Mr. John", 
        contactLastName: "Doe", 
        phone: "12345678",
        addressLine1: "1234 Street",
        city: "City",
        country: "Country",
    };

    Customer.query().insert(customerToCreate).then(customer => {
        Customer.query().findById(customer.customerNumber).then(console.log);

        Customer.query().where("customerName", customer.customerName)
            .then((customer) => console.log(customer[0].contactFirstName));
    });
});

// Example 2: Work with relations
const Employee = require("./models/Employee.js");
const Office = require("./models/Office.js");

const officeToCreate = {
    officeCode: "1",
    city: "City",
    phone: "12345678",
    addressLine1: "1234 Street",
    country: "Country",
    postalCode: "1234",
    territory: "Territory",
};

Office.query().insert(officeToCreate).then((office) => {
    const employeeToCreate = {
        employeeNumber: 1,
        firstName: "John",
        lastName: "Doe",
        extension: "123",
        email: "",
        jobTitle: "Sales Rep",
        officeCode: office.officeCode,
    };

    Employee.query().insert(employeeToCreate).then((employee) => {
        console.log('Employee inserted:', employee);
    });
});


