import type { Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit';


export const actions: Actions = {
  login: async ({ request, cookies}) => {
    const data = await request.formData();
    const email = data.get('email')?.toString();
    const password = data.get('password')?.toString();

    if (!email || !password) {
      return fail(400, { error: 'Todos os campos são obrigatórios.'});
    }

    const body = new URLSearchParams();
    body.append('username', email);
    body.append('password', password);

    const res = await fetch('http://localhost:8000/auth', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: body.toString()
    });

    if (!res.ok) {
      return fail(
        res.status,
        {
          success: false,
          erro: 'Login inválido'
        }
      );
    }

    const result = await res.json();

    cookies.set('token', result.access_token, {
      path: '/',
      httpOnly: true,
      sameSite: 'lax',
      maxAge: 60 * 60 * 24
    });
    
    throw redirect(303, '/home');
  }
};
