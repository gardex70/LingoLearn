<!-- src/routes/+layout.svelte -->
<script>
    import { page } from '$app/state';
    
    // Itens do menu
    const menuItems = [
        { name: 'Dashboard', href: '/app' },
        { name: 'Perfil', href: '/profile' },
        { name: 'Configurações', href: '/app/settings' },
        { name: 'Sair', href: '/logout' }
    ];
</script>

<div class="layout">
    <!-- Barra lateral com menu -->
    <aside class="sidebar">
        <nav class="menu">
            <div class="logo">
                <h1>Minha App</h1>
            </div>
            
            <ul>
                {#each menuItems as item}
                    <li>
                        <a 
                            href={item.href} 
                            class:active={page.url.pathname === item.href}
                        >
                            {item.name}
                        </a>
                    </li>
                {/each}
            </ul>
        </nav>
    </aside>

    <!-- Conteúdo principal -->
    <main class="content">
        <slot />
    </main>
</div>

<style>
    .layout {
        display: flex;
        min-height: 100vh;
    }
    
    .sidebar {
        width: 250px;
        background-color: #2c3e50;
        color: white;
        padding: 1rem;
    }
    
    .logo {
        padding: 1rem;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .menu ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .menu li {
        margin-bottom: 0.5rem;
    }
    
    .menu a {
        display: block;
        padding: 0.75rem 1rem;
        color: white;
        text-decoration: none;
        border-radius: 4px;
        transition: background-color 0.2s;
    }
    
    .menu a:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .menu a.active {
        background-color: #3498db;
        font-weight: bold;
    }
    
    .content {
        flex: 1;
        padding: 2rem;
        background-color: #f5f5f5;
    }
</style>