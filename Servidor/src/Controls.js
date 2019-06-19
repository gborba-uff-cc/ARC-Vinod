import React from 'react';

const Controls = props => {
    return (
        <div className = "ui card">
            <div className = "content">
                {props.children}
            </div>
            <div className = "extra content">
                <div className = "ui two buttons">
                    <div className = "ui basic green button">
                        confirmar
                    </div>
                    <div className = "ui basic red button">
                        cancelar
                    </div>
                </div>
            </div>
        
        </div>

    );
};

export default Controls;