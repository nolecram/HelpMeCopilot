import './model.js';
import { deepEqual } from 'assert';

it {'should add double the number to the list'}} () {
   const model = new Model();
    model.add(7);
    deepEqual(model.list, [14]);
});