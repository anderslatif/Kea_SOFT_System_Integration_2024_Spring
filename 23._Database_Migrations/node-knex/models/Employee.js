const { Model } = require('objection');
const Office = require('./Office.js');


class Employee extends Model {

    static get tableName() {
        return 'employees';
    }

    static get idColumn() {
        return 'employeeNumber';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                employeeNumber: { type: 'number' },
                lastName: { type: 'string' },
                firstName: { type: 'string' },
                extension: { type: 'string' },
                email: { type: 'string' },
                officeCode: { type: 'string' },
                reportsTo: { type: 'number' },
                jobTitle: { type: 'string' },
            
            }
        };
    }
    static get relationMappings() {
      
        return {
          office: {
                    relation: Model.ManyToManyRelation,
                    modelClass: Office,
                    join: {
                        from: 'employees.officeCode',
                        to: 'offices.officeCode'
                    }
                },employee: {
                    relation: Model.ManyToManyRelation,
                    modelClass: Employee,
                    join: {
                        from: 'employees.reportsTo',
                        to: 'employees.employeeNumber'
                    }
                }
        };
    }
}

module.exports = Employee;
