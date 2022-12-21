import React, { useState } from "react";

const SignIn = () => {
    const [user, setUser] = useState(null);

    const onSignIn = (googleUser) => {
        const profile = googleUser.getBasicProfile();
        setUser({
            id: profile.getId(),
            name: profile.getName(),
            email: profile.getEmail(),
        });
    };

    return (
        <div>
            {user ? (
                <p>Welcome, {user.name}</p>
            ) : (
                <div className="g-signin2" data-onsuccess={onSignIn}></div>
            )}
        </div>
    );
};

export default SignIn;
