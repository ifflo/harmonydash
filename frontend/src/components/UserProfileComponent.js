// src/components/UserProfileComponent.js
import React from 'react';
import useUserProfiles from '../hooks/useUserProfiles';

function UserProfileComponent() {
    const { userProfiles, loading } = useUserProfiles();

    if (loading) return <div>Loading...</div>;

    return (
        <div>
            <h2>User Profiles</h2>
            <ul>
                {userProfiles.map(profile => (
                    <li key={profile.id}>{profile.name} - {profile.email}</li>
                ))}
            </ul>
        </div>
    );
}

export default UserProfileComponent;