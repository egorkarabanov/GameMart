import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    items: [],
};

const likeSlice = createSlice({
    name: 'like',
    initialState,
    reducers: {
        toggleLikeItem(state, action) {
            if (state.items.find(obj => obj.pk === action.payload.pk)) {
                state.items = state.items.filter(obj => obj.pk !== action.payload.pk);
            } else {
                state.items.push({...action.payload});
            }
        },
        clearLike(state, action) {
            state.items = [];
        },
        addManyLikeItems(state, action) {
            const newData = action.payload.map(obj => obj.game).map(obj => ({...obj, isNew: true}));
            state.items = state.items.concat(newData);
        }
    },
});

export const {toggleLikeItem, clearLike, addManyLikeItems} = likeSlice.actions;
export default likeSlice.reducer;

