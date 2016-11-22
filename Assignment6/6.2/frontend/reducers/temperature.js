export default (state = [], action) => {
    switch (action.type){
        case 'TEMPERATURE_LOADING':
            return action.payload;
        case 'TEMPERATURE_UPDATED':
            return action.payload
        default : return state;

    }
};