import React, {useEffect} from "react";
import styles from './GameBlock.module.scss';
import {GameCart} from "./GameCart";
import {useDispatch, useSelector} from "react-redux";
import {getProducts} from "../../redux/slices/productSlice";

export const GameBlock = () => {
    const dispatch = useDispatch();
    const items = useSelector((state) => state.product.items);
    useEffect(() => {
        dispatch(getProducts());
    }, []);

    const items_display = items.map((obj) => <GameCart key={obj.pk} {...obj}/>);
    return (
        <div className={`container`}>
            <div className={styles.gridContainer}>
                {items_display}
            </div>
        </div>
    );
}