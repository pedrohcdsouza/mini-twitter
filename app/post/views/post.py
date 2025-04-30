from rest_framework import generics, permissions
from ..models import Post
from ..serializers import PostSerializer

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

class PostLikeView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        serializer.save()

class PostFeedView(generics.ListAPIView): # FALTA ADICIONAR: SÓ APARECER QUEM É VOCÊ SEGUE

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        
        user = self.request.user
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')