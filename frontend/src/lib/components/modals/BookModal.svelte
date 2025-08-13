<script lang="ts">
    // TODO adicionar validação de texto ao salvar
	import { page } from '$app/state';
	import { Tab } from '$lib/components/layout';
	import { Button, Input, Upload } from '$lib/components/ui';
    import { X, BookOpen, Check } from '@lucide/svelte';
	

    interface Book {
        id: number
        title: string
        author: string
        language: string
        userId: number
    }

    interface BookFormData {
        title: string
        author: string
        language: string
        content: string
        user_id: string
    }

    interface BookModalProps {
        isOpen: boolean
        onClose: () => void
        onSave: (book: BookFormData) => void
        book?: Book | null
    }


    let { isOpen, onClose, onSave, book }: BookModalProps = $props();

    let bookForm: BookFormData = $state({
        author:'',
        content:'',
        language:'',
        title:'',
        user_id:page.data.user.id
    });

    let tabs = [
        {label: 'Upload', content: uploadTab},
        {label: 'Detalhes', content: detailTab}
    ]

    function handleOnClose(event: MouseEvent) {
        if (event.target === event.currentTarget) {
            onClose();
        }
    }

    function handleOnKeydown(event: KeyboardEvent) {
        if(event.key === 'Escape') {
            onClose();
        }
    }

    function handleTextUpload(fileContent: string) {
       bookForm.content = fileContent;
    }

    async function handleSave() {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/texts`, {
            method: 'POST',
            headers: {
		        'Content-Type': 'application/json',
	        },
            body: JSON.stringify(bookForm)
        });

        console.log(res);

    }

    $inspect(bookForm);

</script>

{#snippet uploadTab()}
    <Upload onUpload={handleTextUpload}/>
{/snippet}
{#snippet detailTab()}
    <div class="tab-detail">
        <div class="book-form">
            <h2>Informações Básicas</h2>
            <div class="tab-detail-inputs">
                <Input
                    label="Título"
                    placeholder="Digite o Título do livro"
                    type='text'
                    mandatory={true}
                    variant='fullWidth'
                    bind:value={bookForm.title}
                />
                <Input
                    label="Autor"
                    placeholder="Digite o Autor do livro"
                    type="text"
                    mandatory={true}
                    variant='fullWidth'
                    bind:value={bookForm.author}
                />
                <Input
                    label="Idioma"
                    placeholder="Digite o Idioma do livro"
                    type="text"
                    mandatory={true}
                    variant='fullWidth'
                    bind:value={bookForm.language}
                />
            </div>
        </div>
        <div class="book-image">

        </div>
    </div>
    
{/snippet}

{#if isOpen}
    <div 
        class="modal-overlay"
        onclick={handleOnClose}
        onkeydown={handleOnKeydown}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        tabindex="0"
    >
        <div class="modal-container">
            <div class="modal-header">
                <div class="modal-title">
                    <div class="modal-title-icon">
                        <BookOpen/>
                    </div>
                    <div>
                        <h3>Adicionar Novo Livro</h3>
                        <p>Adicione um novo livro à sua biblioteca</p>
                    </div>
                </div>
                <div class="modal-close">
                    <button onclick={onClose} class="close-button"><X size={20}/></button>
                </div>
            </div>

            <div class="modal-tabs">
                <Tab items={tabs} />
            </div>

            <div class="modal-footer">
                <Button
                    onclick={onClose}
                    variant='outline'
                    size='small'
                >
                    Fechar
                </Button>
                <Button
                    size='small'
                    onclick={handleSave}
                >
                    <Check/> Adicionar Livro
                </Button>
            </div>
        </div>
    </div>
{/if}

<style>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal-container {
        background: var(--background-white);
        border-radius: 8px;
        width: 90%;
        max-width: 800px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .modal-header {
        border-bottom: 1px solid var(--border-light);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
    }

    .modal-header p {
        font-size: 14px;
    }

    .modal-header h3 {
        font-size: 20px;
    }

    .modal-title {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
        
    }

    .modal-title-icon {
        background-color: var(--primary-blue-light);
        color: var(--primary-blue);
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .close-button {
        background: none;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 6px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .close-button:hover {
        transition: 0.2s ease;
        
        background-color: var(--background-gray);
    }

    .tab-detail {
        width: 100%;
    }

    .tab-detail-inputs {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .modal-footer {
        padding: 1rem;
        border-top: 1px solid var(--border-light);
        display: flex;
        justify-content: flex-end;
        gap: 1rem;
    }

</style>