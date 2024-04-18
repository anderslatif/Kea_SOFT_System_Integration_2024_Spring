const { Model } = require('objection');

class Products2 extends Model {

    static get tableName() {
        return 'products2';
    }

    static get idColumn() {
        return 'id';
    }


    static get jsonSchema() {
        return {
            type: 'object',
            required: [],

            properties: {
                id: { type: 'number' },
                price: { type: 'string' },
                name: { type: 'string' },
            
            }
        };
    }
    
}

module.exports = Products2;
