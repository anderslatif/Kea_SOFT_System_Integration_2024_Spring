const { Model } = require('objection');
const Customer = require('./Customer.js');

class Order extends Model {

    static get tableName() {
        return 'orders';
    }

    static get idColumn() {
        return 'orderNumber';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                orderNumber: { type: 'number' },
                orderDate: { type: 'date' },
                requiredDate: { type: 'date' },
                shippedDate: { type: 'date' },
                status: { type: 'string' },
                comments: { type: 'string' },
                customerNumber: { type: 'number' },
            
            }
        };
    }
    static get relationMappings() {
      
        return {
          customer: {
                    relation: Model.ManyToManyRelation,
                    modelClass: Customer,
                    join: {
                        from: 'orders.customerNumber',
                        to: 'customers.customerNumber'
                    }
                }
        };
    }
}

module.exports = Order;
