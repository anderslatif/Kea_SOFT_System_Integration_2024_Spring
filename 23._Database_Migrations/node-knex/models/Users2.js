const { Model } = require('objection');

class Users2 extends Model {

    static get tableName() {
        return 'users2';
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
                first_name: { type: 'string' },
                last_name: { type: 'string' },
            
            }
        };
    }
    
}

module.exports = Users2;
