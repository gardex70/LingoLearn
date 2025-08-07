<script lang="ts">
    import Sidebar from "$lib/components/layout/Sidebar/Sidebar.svelte";
	import { Button, Search } from "$lib/components/ui";
	import BookList from "$lib/components/ui/BookList.svelte";
    import { Upload, Grid3x3, List } from "@lucide/svelte";
	
    type View = 'grid' | 'list';
    let view: View = $state('list');

</script>

<main>
    <Sidebar
    user = {{
        name: "Gabriel",
        email: "gabrielpabrahao@gmail.com"
    }}
    />
    <section>
        <header>
            <div class="header-title">
                <h1>Minha Biblioteca</h1>
                <p>12 livros &bull; 12 em progresso</p>
            </div>
            <Button
                size='small'
            >
                <Upload size={20}/>
                Adicionar livro
            </Button>
        </header>

        
        <div class="options">
            <Search
                placeholder="Buscar por título, autor ou gênero..."
                size="full-width"
            />

            <select>
                <option>Todos os idiomas</option>
                <option>Português</option>
                <option>Inglês</option>
                <option>Espanhol</option>
            </select>

            <select>
                <option>Recente</option>
                <option>Mais antigos</option>
                <option>A-Z</option>
                <option>Z-A</option>
            </select>
            <div class="view">
                <button 
                class="button-left"
                class:active={ view === 'grid'}
                onclick={() => view = 'grid'}
                >
                    <Grid3x3 size={20}/>
                </button>

                <button
                    class="button-right"
                    class:active={ view === 'list'}
                    onclick={() => view = 'list'}
                >
                    <List size={20}/>
                </button>
            </div>
        </div>

        <div class="text-body">
            {#if view == 'grid'}
                <h1>Grid</h1>
            {:else}
                <BookList/>
            {/if}
        </div>
    </section>
</main>
    
   
<style>
    main {
        display: flex;
    }

    section {
        width: 100%;
        padding: 4rem;
    }

    header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .options {
        display: flex;
        gap: 1rem;
    }

    .view {
        display: flex;
        border-collapse: collapse;
    }

    .view button {
        padding: 0.5rem 0.5rem;
        background-color: var(--background-light);
        border-radius: 8px;
        border: 1px solid var(--border);
    }

    .view button.button-left {
        border-top-right-radius: 0 ;
        border-bottom-right-radius: 0;
    }

    .view button.button-right {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
    }

    .view button.active {
        background: var(--primary-blue);
        color: var(--background-white)
    }
</style>