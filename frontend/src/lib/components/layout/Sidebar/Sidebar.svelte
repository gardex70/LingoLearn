<script lang="ts">
    import { User, CircleUserRound, House, LibraryBig, LogOut } from '@lucide/svelte';
    import Logo from '$lib/components/ui/Logo.svelte';
	import SidebarItem from './SidebarItem.svelte';
    import type { SidebarItemType } from './SidebarItem.svelte'; 
	import { page } from '$app/state';

    interface UserType {
        avatar?: string
        name?: string
        email?: string
    }

    interface SidebarProps {
        user: UserType
    }

    let { user }: SidebarProps = $props();
    
    const GROUP_REGEX = /\([^)]*\)\//g;
    let currentPage = page.route.id?.replace(GROUP_REGEX, '');

    const items: SidebarItemType[] = [
		{ page: "/home", label: "Início", icon: House},
		{ page: "/texts", label: "Biblioteca", icon: LibraryBig }
	];
    let updatedItems = items.map(item => ({
        ...item,
        isActive: item.page === currentPage
    }));

    const footerItems: SidebarItemType[] = [
        {page: "/profile", label: "Perfil", icon: User},
        {page: "/login", label: "Sair", icon: LogOut, style: "red"}
    ]
    let updatedFooterItems = footerItems.map(item => ({
        ...item,
        isActive: item.page === currentPage
    }));
</script>

<aside class="sidebar">
    <div class="header">
        <Logo/>
    </div>

    <div class="userSection">
        <div class="userInfo">
            {#if user?.avatar}
                <img src={user.avatar} alt={user.name} class="avatar">
            {:else}
                <CircleUserRound size={32}/>
            {/if}
          <div class="userDetails">
            <span class=userName>{user?.name}</span>
            <span class=userEmail>{user?.email}</span>
          </div>
        </div>
    </div>

    <nav>
        {#each updatedItems as item}
            <SidebarItem {item}/>
        {/each}
    </nav>

    <div class="footer">
        <nav>
            {#each updatedFooterItems as item}
            <SidebarItem {item}/>
        {/each}
        </nav>
    </div>
</aside>


<style>
    .sidebar {
    width: 280px;
    height: 100vh;
    background: var(--background-white);
    border-right: 1px solid var(--border-light);
    display: flex;
    flex-direction: column;
    z-index: 100;
}

    .header {
        padding: 1.5rem;
        border-bottom: 1px solid var(--border-light);
    }

    .userSection {
        padding: 1.5rem;
        border-bottom: 1px solid var(--border-light);
    }

    .userInfo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: cover;
    }

    .userDetails {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }

    .userName {
        font-weight: 600;
        color: var(--text-primary);
    }

    .userEmail {
        font-size: 0.875rem;
        color: var(--text-secondary);
    }

    nav {
        flex: 1;
        padding: 1rem 0;
    }

    .footer {
        padding: 1rem;
        padding-left: 0;
        border-top: 1px solid var(--border-light);
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
</style>