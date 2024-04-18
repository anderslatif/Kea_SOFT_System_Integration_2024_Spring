const { Model } = require('objection');

class Orderdetail extends Model {

    static get tableName() {
        return 'orderdetails';
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
                productCode: { type: 'string' },
                quantityOrdered: { type: 'number' },
                priceEach: { type: 'string' },
                orderLineNumber: { type: 'number' },
            
            }
        };
    }
    
}

module.exports = Orderdetail;
