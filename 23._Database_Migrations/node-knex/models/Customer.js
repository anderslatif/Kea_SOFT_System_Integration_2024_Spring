const { Model } = require('objection');
const Employee = require('./Employee.js');

class Customer extends Model {

    static get tableName() {
        return 'customers';
    }

    static get idColumn() {
        return 'customerNumber';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                customerNumber: { type: 'number' },
                customerName: { type: 'string' },
                contactLastName: { type: 'string' },
                contactFirstName: { type: 'string' },
                phone: { type: 'string' },
                addressLine1: { type: 'string' },
                addressLine2: { type: 'string' },
                city: { type: 'string' },
                state: { type: 'string' },
                postalCode: { type: 'string' },
                country: { type: 'string' },
                salesRepEmployeeNumber: { type: 'number' },
                creditLimit: { type: 'string' },
            
            }
        };
    }
    static get relationMappings() {
      
        return {
          employee: {
                    relation: Model.ManyToManyRelation,
                    modelClass: Employee,
                    join: {
                        from: 'customers.salesRepEmployeeNumber',
                        to: 'employees.employeeNumber'
                    }
                }
        };
    }
}

module.exports = Customer;
