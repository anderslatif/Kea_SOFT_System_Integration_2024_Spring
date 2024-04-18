const { Model } = require('objection');

class Productline extends Model {

    static get tableName() {
        return 'productlines';
    }

    static get idColumn() {
        return 'productLine';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                productLine: { type: 'string' },
                textDescription: { type: 'string' },
                htmlDescription: { type: 'string' },
                image: { type: 'buffer' },
            
            }
        };
    }
    
}

module.exports = Productline;
