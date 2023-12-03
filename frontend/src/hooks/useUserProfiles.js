// src/hooks/useUserProfiles.js
import { useState, useEffect } from 'react';
import { getUserProfiles } from '../apiService';

const useUserProfiles = () => {
    const [userProfiles, setUserProfiles] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getUserProfiles()
            .then(response => {
                setUserProfiles(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching user profiles!', error);
                setLoading(false);
            });
    }, []);

    return { userProfiles, loading };
};

export default useUserProfiles;