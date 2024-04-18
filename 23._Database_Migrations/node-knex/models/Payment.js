const { Model } = require('objection');

class Payment extends Model {

    static get tableName() {
        return 'payments';
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
                checkNumber: { type: 'string' },
                paymentDate: { type: 'date' },
                amount: { type: 'string' },
            
            }
        };
    }
    
}

module.exports = Payment;
