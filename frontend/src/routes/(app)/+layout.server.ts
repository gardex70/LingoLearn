import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load = (async ({ cookies }) => {
    const token = cookies.get('token');
    
    if (!token) {
        throw redirect(303, '/login');
    }

    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/auth`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (!res.ok) {
            throw redirect(303, '/login');
        }

        const userData = await res.json();

        return {
            user: userData,
            isAuthenticated: true
        }

    } catch (err) {
        cookies.delete('token', { path: '/'});
        
        throw redirect(303, '/login');
    }
    
}) satisfies LayoutServerLoad;