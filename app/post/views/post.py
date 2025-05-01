from rest_framework import generics, permissions
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.exceptions import PermissionDenied

# O USUÁRIO NÃO ESTÁ CONSEGUINDO VER POSTS QUE ELE NÃO CRIOU, MESMO QUE SEJA DE ALGUÉM QUE ELE SIGA (CORRIGIR!)
 
# This view handles the creation of new posts

class PostCreateView(generics.CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# This view handles the update of existing posts        

class PostUpdateView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You can't edit this post.")
        serializer.save()

# This view handles the deletion of posts

class PostDeleteView(generics.DestroyAPIView):
            
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You can't delete this post.")
        instance.delete()

class PostDetailView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.author: # ATENÇÃO, REFAZER ESSA PARTE PARA A PESSOA NÃO VER POST QUE NÃO É DELA OU NÃO É POR ALGUEM QUE É SEGUIDO
            raise PermissionDenied("You can't view this post.")
        return obj
