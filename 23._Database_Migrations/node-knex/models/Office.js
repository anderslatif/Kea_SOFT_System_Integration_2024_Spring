const { Model } = require('objection');

class Office extends Model {

    static get tableName() {
        return 'offices';
    }

    static get idColumn() {
        return 'officeCode';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                officeCode: { type: 'string' },
                city: { type: 'string' },
                phone: { type: 'string' },
                addressLine1: { type: 'string' },
                addressLine2: { type: 'string' },
                state: { type: 'string' },
                country: { type: 'string' },
                postalCode: { type: 'string' },
                territory: { type: 'string' },
            
            }
        };
    }
    
}

module.exports = Office;
