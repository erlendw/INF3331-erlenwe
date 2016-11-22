import { combineReducers } from 'redux'

import temperature from './temperature'
import co2 from './co2'

const chatApp = combineReducers({
    temperature : temperature,
    co2:co2
})

export default chatApp