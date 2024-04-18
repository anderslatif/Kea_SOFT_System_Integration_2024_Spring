/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.up = function(knex) {
    return knex.schema    
        .createTable('offices', (table) => {
           table.string('officeCode').notNullable().primary();
           table.string('city').notNullable();
           table.string('phone').notNullable();
           table.string('addressLine1').notNullable();
           table.string('addressLine2');
           table.string('state');
           table.string('country').notNullable();
           table.string('postalCode').notNullable();
           table.string('territory').notNullable();

        })    
        .createTable('employees', (table) => {
           table.integer('employeeNumber').notNullable().primary();
           table.string('lastName').notNullable();
           table.string('firstName').notNullable();
           table.string('extension').notNullable();
           table.string('email').notNullable();
           table.string('officeCode').notNullable().index();
           table.foreign('officeCode').references('officeCode').inTable('offices');
           table.integer('reportsTo').index();
           table.foreign('reportsTo').references('employeeNumber').inTable('employees');
           table.string('jobTitle').notNullable();

        })    
        .createTable('customers', (table) => {
           table.integer('customerNumber').notNullable().primary();
           table.string('customerName').notNullable();
           table.string('contactLastName').notNullable();
           table.string('contactFirstName').notNullable();
           table.string('phone').notNullable();
           table.string('addressLine1').notNullable();
           table.string('addressLine2');
           table.string('city').notNullable();
           table.string('state');
           table.string('postalCode');
           table.string('country').notNullable();
           table.integer('salesRepEmployeeNumber').index();
           table.foreign('salesRepEmployeeNumber').references('employeeNumber').inTable('employees');
           table.decimal('creditLimit');

        })    
        .createTable('orderdetails', (table) => {
           table.integer('orderNumber').notNullable().primary();
           table.string('productCode').notNullable().primary();
           table.integer('quantityOrdered').notNullable();
           table.decimal('priceEach').notNullable();
           table.integer('orderLineNumber').notNullable();

        })    
        .createTable('orders', (table) => {
           table.integer('orderNumber').notNullable().primary();
           table.date('orderDate').notNullable();
           table.date('requiredDate').notNullable();
           table.date('shippedDate');
           table.string('status').notNullable();
           table.string('comments');
           table.integer('customerNumber').notNullable().index();
           table.foreign('customerNumber').references('customerNumber').inTable('customers');

        })    
        .createTable('payments', (table) => {
           table.integer('customerNumber').notNullable().primary();
           table.string('checkNumber').notNullable().primary();
           table.date('paymentDate').notNullable();
           table.decimal('amount').notNullable();

        })    
        .createTable('productlines', (table) => {
           table.string('productLine').notNullable().primary();
           table.string('textDescription');
           table.string('htmlDescription');
           table.binary('image');

        })    
        .createTable('products', (table) => {
           table.string('productCode').notNullable().primary();
           table.string('productName').notNullable();
           table.string('productLine').notNullable().index();
           table.foreign('productLine').references('productLine').inTable('productlines');
           table.string('productScale').notNullable();
           table.string('productVendor').notNullable();
           table.string('productDescription').notNullable();
           table.integer('quantityInStock').notNullable();
           table.decimal('buyPrice').notNullable();
           table.decimal('MSRP').notNullable();

        })        
};

exports.down = function(knex) {
    return knex.schema
           .dropTable('products')
           .dropTable('productlines')
           .dropTable('payments')
           .dropTable('orders')
           .dropTable('orderdetails')
           .dropTable('customers')
           .dropTable('employees')
           .dropTable('offices');
};
