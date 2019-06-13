import React from 'react';
import faker from 'faker';


const CommentDetail = (props) => {
    return (
        <div className ="comment">
                <a href = "/" className = "avatar">
                    <img alt = "avatar" src={faker.image.avatar()}/>
                </a>
                <div className = "content">
                    <a className = "author">
                        {props.balao}
                    </a>
                    <div className = "metadata">
                        <span className="date">
                            {props.coord}
                        </span>
                    </div>

                    <div className = "text">
                        Sinal BOM
                    </div>
                </div>
            </div>


    );
};

export default CommentDetail;