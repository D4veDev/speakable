import React, { useEffect } from 'react';

export const Home = () => {

    useEffect(() => {
            document.querySelector("#room-name-input").focus();

            // If you hit "enter" on the keyboard, trigger the click method
            document.querySelector("#room-name-input").onkeypress = function (e) {
                console.log("keycode:" + e.keyCode);
                if (e.keyCode === 13) {
                    document.querySelector("#room-name-submit").click();
                }
            };

            // When you submit the form, redirect the user to the room page
            document.querySelector("#room-name-submit").onclick = function (e) {
                var roomName = document.querySelector("#room-name-input").value;
                var userName = document.querySelector("#username-input").value;
                var param = userName === "" ? "/" : "/?username=" + userName;
                window.location.replace(roomName + param);
            };
    }, []);

    return (
        <section className="section">
            <div className="container">
                <div className="columns is-multiline">
                    <div className="column is-6 is-offset-3 mb-6">
                        <section className="hero is-primary">
                            <div className="hero-body">
                                <p className="title">DisabilityHub</p>
                                <p className="subtitle">
                                    A simple chat built with Django, Channels
                                    and Redis
                                </p>
                            </div>
                        </section>
                    </div>

                    <div className="column is-4 is-offset-4">
                        <div className="field">
                            <label>Room name</label>

                            <div className="control">
                                <input
                                    className="input"
                                    type="text"
                                    placeholder="Room name"
                                    id="room-name-input"
                                />
                            </div>
                        </div>

                        <div className="field">
                            <label>Username</label>

                            <div className="control">
                                <input
                                    className="input"
                                    type="text"
                                    placeholder="Username"
                                    id="username-input"
                                />
                            </div>
                        </div>

                        <div className="field">
                            <div className="control">
                                <a className="button is-info" id="room-name-submit">
                                  Submit
                                  </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}