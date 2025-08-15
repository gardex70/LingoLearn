<script lang="ts">
	import { TextCard } from ".";
	import type { TextType } from "./TextCard.svelte";
    
    interface BookListProps {
        texts: TextType[]
    }
    let { texts }: BookListProps = $props();
    let t = $state();
    function handleOnDetail(textId: number) {
        t = textId
    }

    $inspect(t);

</script>
{#each texts as text}
    <div class="wrapper">
        <TextCard
            {text}
            onDetail={handleOnDetail}
        />
    </div>
{/each}


<style>
    .wrapper {
        margin-top: 1rem;
    }
</style>
